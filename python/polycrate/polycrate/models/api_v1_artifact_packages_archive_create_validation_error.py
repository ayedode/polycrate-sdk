from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifact_packages_archive_create_annotations_error_component import (
        ApiV1ArtifactPackagesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_archived_at_error_component import (
        ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_archived_by_error_component import (
        ApiV1ArtifactPackagesArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_archived_error_component import (
        ApiV1ArtifactPackagesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_archived_reason_error_component import (
        ApiV1ArtifactPackagesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_created_by_component_error_component import (
        ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_created_by_user_error_component import (
        ApiV1ArtifactPackagesArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_criticality_error_component import (
        ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_debug_mode_error_component import (
        ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_display_name_error_component import (
        ApiV1ArtifactPackagesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_kind_error_component import (
        ApiV1ArtifactPackagesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_labels_error_component import (
        ApiV1ArtifactPackagesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactPackagesArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_managed_by_content_type_error_component import (
        ApiV1ArtifactPackagesArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_managed_by_object_id_error_component import (
        ApiV1ArtifactPackagesArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_modified_by_user_error_component import (
        ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_name_error_component import (
        ApiV1ArtifactPackagesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_non_field_errors_error_component import (
        ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_platform_dns_record_created_error_component import (
        ApiV1ArtifactPackagesArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_platform_service_error_component import (
        ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_provider_error_component import (
        ApiV1ArtifactPackagesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_provider_id_error_component import (
        ApiV1ArtifactPackagesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_provider_reference_error_component import (
        ApiV1ArtifactPackagesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_raw_data_error_component import (
        ApiV1ArtifactPackagesArchiveCreateRawDataErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_reconciliation_enabled_error_component import (
        ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_sla_availability_error_component import (
        ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_sla_target_error_component import (
        ApiV1ArtifactPackagesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_sla_window_days_error_component import (
        ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_slo_availability_error_component import (
        ApiV1ArtifactPackagesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_slo_target_error_component import (
        ApiV1ArtifactPackagesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_slo_window_days_error_component import (
        ApiV1ArtifactPackagesArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_target_availability_error_component import (
        ApiV1ArtifactPackagesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_archive_create_tolerations_error_component import (
        ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactPackagesArchiveCreateValidationError")


@_attrs_define
class ApiV1ArtifactPackagesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactPackagesArchiveCreateAnnotationsErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateArchivedByErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateArchivedErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateArchivedReasonErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateCreatedByUserErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateDisplayNameErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateKindErrorComponent | ApiV1ArtifactPackagesArchiveCreateLabelsErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateNameErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1ArtifactPackagesArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateProviderErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateProviderIdErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateProviderReferenceErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateRawDataErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateSlaTargetErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateSloTargetErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateSloWindowDaysErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactPackagesArchiveCreateAnnotationsErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateArchivedByErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateArchivedErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateArchivedReasonErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateCreatedByUserErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateDisplayNameErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateKindErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateLabelsErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateNameErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ArtifactPackagesArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateProviderErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateProviderIdErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateProviderReferenceErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateRawDataErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateSlaTargetErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateSloTargetErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateSloWindowDaysErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifact_packages_archive_create_annotations_error_component import (
            ApiV1ArtifactPackagesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_archived_at_error_component import (
            ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_archived_by_error_component import (
            ApiV1ArtifactPackagesArchiveCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_archived_error_component import (
            ApiV1ArtifactPackagesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_archived_reason_error_component import (
            ApiV1ArtifactPackagesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_created_by_component_error_component import (
            ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_criticality_error_component import (
            ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_debug_mode_error_component import (
            ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_display_name_error_component import (
            ApiV1ArtifactPackagesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_kind_error_component import (
            ApiV1ArtifactPackagesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_labels_error_component import (
            ApiV1ArtifactPackagesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactPackagesArchiveCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_managed_by_content_type_error_component import (
            ApiV1ArtifactPackagesArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_managed_by_object_id_error_component import (
            ApiV1ArtifactPackagesArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_modified_by_user_error_component import (
            ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_name_error_component import (
            ApiV1ArtifactPackagesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_non_field_errors_error_component import (
            ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactPackagesArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_platform_service_error_component import (
            ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_provider_error_component import (
            ApiV1ArtifactPackagesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_provider_id_error_component import (
            ApiV1ArtifactPackagesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_provider_reference_error_component import (
            ApiV1ArtifactPackagesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_raw_data_error_component import (
            ApiV1ArtifactPackagesArchiveCreateRawDataErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_sla_availability_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_sla_target_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_sla_window_days_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_slo_availability_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_slo_target_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_slo_window_days_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_target_availability_error_component import (
            ApiV1ArtifactPackagesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_tolerations_error_component import (
            ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactPackagesArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateRawDataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_artifact_packages_archive_create_annotations_error_component import (
            ApiV1ArtifactPackagesArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_archived_at_error_component import (
            ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_archived_by_error_component import (
            ApiV1ArtifactPackagesArchiveCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_archived_error_component import (
            ApiV1ArtifactPackagesArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_archived_reason_error_component import (
            ApiV1ArtifactPackagesArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_created_by_component_error_component import (
            ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_created_by_user_error_component import (
            ApiV1ArtifactPackagesArchiveCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_criticality_error_component import (
            ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_debug_mode_error_component import (
            ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_display_name_error_component import (
            ApiV1ArtifactPackagesArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_kind_error_component import (
            ApiV1ArtifactPackagesArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_labels_error_component import (
            ApiV1ArtifactPackagesArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactPackagesArchiveCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_managed_by_content_type_error_component import (
            ApiV1ArtifactPackagesArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_managed_by_object_id_error_component import (
            ApiV1ArtifactPackagesArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_modified_by_user_error_component import (
            ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_name_error_component import (
            ApiV1ArtifactPackagesArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_non_field_errors_error_component import (
            ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactPackagesArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_platform_service_error_component import (
            ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_provider_error_component import (
            ApiV1ArtifactPackagesArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_provider_id_error_component import (
            ApiV1ArtifactPackagesArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_provider_reference_error_component import (
            ApiV1ArtifactPackagesArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_raw_data_error_component import (
            ApiV1ArtifactPackagesArchiveCreateRawDataErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_sla_availability_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_sla_target_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_sla_window_days_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_slo_availability_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_slo_target_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_slo_window_days_error_component import (
            ApiV1ArtifactPackagesArchiveCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_target_availability_error_component import (
            ApiV1ArtifactPackagesArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_packages_archive_create_tolerations_error_component import (
            ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactPackagesArchiveCreateAnnotationsErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateArchivedByErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateArchivedErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateArchivedReasonErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateCreatedByUserErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateDisplayNameErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateKindErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateLabelsErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateNameErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ArtifactPackagesArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateProviderErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateProviderIdErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateProviderReferenceErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateRawDataErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateSlaTargetErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateSloTargetErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateSloWindowDaysErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_0 = (
                        ApiV1ArtifactPackagesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_1 = (
                        ApiV1ArtifactPackagesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_2 = (
                        ApiV1ArtifactPackagesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_3 = (
                        ApiV1ArtifactPackagesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_4 = (
                        ApiV1ArtifactPackagesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_5 = (
                        ApiV1ArtifactPackagesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_6 = (
                        ApiV1ArtifactPackagesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_7 = (
                        ApiV1ArtifactPackagesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_8 = (
                        ApiV1ArtifactPackagesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_9 = (
                        ApiV1ArtifactPackagesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_10 = (
                        ApiV1ArtifactPackagesArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_11 = (
                        ApiV1ArtifactPackagesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_12 = (
                        ApiV1ArtifactPackagesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_13 = (
                        ApiV1ArtifactPackagesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_14 = (
                        ApiV1ArtifactPackagesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_15 = (
                        ApiV1ArtifactPackagesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_16 = (
                        ApiV1ArtifactPackagesArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_17 = (
                        ApiV1ArtifactPackagesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_18 = (
                        ApiV1ArtifactPackagesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_19 = (
                        ApiV1ArtifactPackagesArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_20 = (
                        ApiV1ArtifactPackagesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_21 = (
                        ApiV1ArtifactPackagesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_22 = (
                        ApiV1ArtifactPackagesArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_23 = (
                        ApiV1ArtifactPackagesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_24 = (
                        ApiV1ArtifactPackagesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_25 = (
                        ApiV1ArtifactPackagesArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_26 = (
                        ApiV1ArtifactPackagesArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_27 = (
                        ApiV1ArtifactPackagesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_28 = (
                        ApiV1ArtifactPackagesArchiveCreateRawDataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_29 = (
                        ApiV1ArtifactPackagesArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_30 = (
                        ApiV1ArtifactPackagesArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_archive_create_error_type_31 = (
                        ApiV1ArtifactPackagesArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifact_packages_archive_create_error_type_32 = (
                    ApiV1ArtifactPackagesArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifact_packages_archive_create_error_type_32

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifact_packages_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifact_packages_archive_create_validation_error.additional_properties = d
        return api_v1_artifact_packages_archive_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
