from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifact_packages_update_annotations_error_component import (
        ApiV1ArtifactPackagesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_archived_at_error_component import (
        ApiV1ArtifactPackagesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_archived_by_error_component import (
        ApiV1ArtifactPackagesUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_archived_error_component import (
        ApiV1ArtifactPackagesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_archived_reason_error_component import (
        ApiV1ArtifactPackagesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_created_by_component_error_component import (
        ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_created_by_user_error_component import (
        ApiV1ArtifactPackagesUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_criticality_error_component import (
        ApiV1ArtifactPackagesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_debug_mode_error_component import (
        ApiV1ArtifactPackagesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_display_name_error_component import (
        ApiV1ArtifactPackagesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_kind_error_component import (
        ApiV1ArtifactPackagesUpdateKindErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_labels_error_component import (
        ApiV1ArtifactPackagesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactPackagesUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_managed_by_content_type_error_component import (
        ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_managed_by_object_id_error_component import (
        ApiV1ArtifactPackagesUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_modified_by_user_error_component import (
        ApiV1ArtifactPackagesUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_name_error_component import (
        ApiV1ArtifactPackagesUpdateNameErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_non_field_errors_error_component import (
        ApiV1ArtifactPackagesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_platform_dns_record_created_error_component import (
        ApiV1ArtifactPackagesUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_platform_service_error_component import (
        ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_provider_error_component import (
        ApiV1ArtifactPackagesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_provider_id_error_component import (
        ApiV1ArtifactPackagesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_provider_reference_error_component import (
        ApiV1ArtifactPackagesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_raw_data_error_component import (
        ApiV1ArtifactPackagesUpdateRawDataErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_reconciliation_enabled_error_component import (
        ApiV1ArtifactPackagesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_sla_availability_error_component import (
        ApiV1ArtifactPackagesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_sla_target_error_component import (
        ApiV1ArtifactPackagesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_sla_window_days_error_component import (
        ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_slo_availability_error_component import (
        ApiV1ArtifactPackagesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_slo_target_error_component import (
        ApiV1ArtifactPackagesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_slo_window_days_error_component import (
        ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_target_availability_error_component import (
        ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_packages_update_tolerations_error_component import (
        ApiV1ArtifactPackagesUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactPackagesUpdateValidationError")


@_attrs_define
class ApiV1ArtifactPackagesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactPackagesUpdateAnnotationsErrorComponent |
            ApiV1ArtifactPackagesUpdateArchivedAtErrorComponent | ApiV1ArtifactPackagesUpdateArchivedByErrorComponent |
            ApiV1ArtifactPackagesUpdateArchivedErrorComponent | ApiV1ArtifactPackagesUpdateArchivedReasonErrorComponent |
            ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponent |
            ApiV1ArtifactPackagesUpdateCreatedByUserErrorComponent | ApiV1ArtifactPackagesUpdateCriticalityErrorComponent |
            ApiV1ArtifactPackagesUpdateDebugModeErrorComponent | ApiV1ArtifactPackagesUpdateDisplayNameErrorComponent |
            ApiV1ArtifactPackagesUpdateKindErrorComponent | ApiV1ArtifactPackagesUpdateLabelsErrorComponent |
            ApiV1ArtifactPackagesUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponent |
            ApiV1ArtifactPackagesUpdateManagedByObjectIdErrorComponent |
            ApiV1ArtifactPackagesUpdateModifiedByUserErrorComponent | ApiV1ArtifactPackagesUpdateNameErrorComponent |
            ApiV1ArtifactPackagesUpdateNonFieldErrorsErrorComponent |
            ApiV1ArtifactPackagesUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponent | ApiV1ArtifactPackagesUpdateProviderErrorComponent |
            ApiV1ArtifactPackagesUpdateProviderIdErrorComponent | ApiV1ArtifactPackagesUpdateProviderReferenceErrorComponent
            | ApiV1ArtifactPackagesUpdateRawDataErrorComponent |
            ApiV1ArtifactPackagesUpdateReconciliationEnabledErrorComponent |
            ApiV1ArtifactPackagesUpdateSlaAvailabilityErrorComponent | ApiV1ArtifactPackagesUpdateSlaTargetErrorComponent |
            ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponent |
            ApiV1ArtifactPackagesUpdateSloAvailabilityErrorComponent | ApiV1ArtifactPackagesUpdateSloTargetErrorComponent |
            ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponent |
            ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponent |
            ApiV1ArtifactPackagesUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactPackagesUpdateAnnotationsErrorComponent
        | ApiV1ArtifactPackagesUpdateArchivedAtErrorComponent
        | ApiV1ArtifactPackagesUpdateArchivedByErrorComponent
        | ApiV1ArtifactPackagesUpdateArchivedErrorComponent
        | ApiV1ArtifactPackagesUpdateArchivedReasonErrorComponent
        | ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponent
        | ApiV1ArtifactPackagesUpdateCreatedByUserErrorComponent
        | ApiV1ArtifactPackagesUpdateCriticalityErrorComponent
        | ApiV1ArtifactPackagesUpdateDebugModeErrorComponent
        | ApiV1ArtifactPackagesUpdateDisplayNameErrorComponent
        | ApiV1ArtifactPackagesUpdateKindErrorComponent
        | ApiV1ArtifactPackagesUpdateLabelsErrorComponent
        | ApiV1ArtifactPackagesUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponent
        | ApiV1ArtifactPackagesUpdateManagedByObjectIdErrorComponent
        | ApiV1ArtifactPackagesUpdateModifiedByUserErrorComponent
        | ApiV1ArtifactPackagesUpdateNameErrorComponent
        | ApiV1ArtifactPackagesUpdateNonFieldErrorsErrorComponent
        | ApiV1ArtifactPackagesUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponent
        | ApiV1ArtifactPackagesUpdateProviderErrorComponent
        | ApiV1ArtifactPackagesUpdateProviderIdErrorComponent
        | ApiV1ArtifactPackagesUpdateProviderReferenceErrorComponent
        | ApiV1ArtifactPackagesUpdateRawDataErrorComponent
        | ApiV1ArtifactPackagesUpdateReconciliationEnabledErrorComponent
        | ApiV1ArtifactPackagesUpdateSlaAvailabilityErrorComponent
        | ApiV1ArtifactPackagesUpdateSlaTargetErrorComponent
        | ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponent
        | ApiV1ArtifactPackagesUpdateSloAvailabilityErrorComponent
        | ApiV1ArtifactPackagesUpdateSloTargetErrorComponent
        | ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponent
        | ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponent
        | ApiV1ArtifactPackagesUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifact_packages_update_annotations_error_component import (
            ApiV1ArtifactPackagesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_archived_at_error_component import (
            ApiV1ArtifactPackagesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_archived_by_error_component import (
            ApiV1ArtifactPackagesUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_archived_error_component import (
            ApiV1ArtifactPackagesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_archived_reason_error_component import (
            ApiV1ArtifactPackagesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_created_by_component_error_component import (
            ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_criticality_error_component import (
            ApiV1ArtifactPackagesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_debug_mode_error_component import (
            ApiV1ArtifactPackagesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_display_name_error_component import (
            ApiV1ArtifactPackagesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_kind_error_component import (
            ApiV1ArtifactPackagesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_labels_error_component import (
            ApiV1ArtifactPackagesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactPackagesUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_managed_by_content_type_error_component import (
            ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_managed_by_object_id_error_component import (
            ApiV1ArtifactPackagesUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_modified_by_user_error_component import (
            ApiV1ArtifactPackagesUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_name_error_component import (
            ApiV1ArtifactPackagesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_non_field_errors_error_component import (
            ApiV1ArtifactPackagesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactPackagesUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_platform_service_error_component import (
            ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_provider_error_component import (
            ApiV1ArtifactPackagesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_provider_id_error_component import (
            ApiV1ArtifactPackagesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_provider_reference_error_component import (
            ApiV1ArtifactPackagesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_raw_data_error_component import (
            ApiV1ArtifactPackagesUpdateRawDataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactPackagesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_sla_availability_error_component import (
            ApiV1ArtifactPackagesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_sla_target_error_component import (
            ApiV1ArtifactPackagesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_sla_window_days_error_component import (
            ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_slo_availability_error_component import (
            ApiV1ArtifactPackagesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_slo_target_error_component import (
            ApiV1ArtifactPackagesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_slo_window_days_error_component import (
            ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_target_availability_error_component import (
            ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_tolerations_error_component import (
            ApiV1ArtifactPackagesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactPackagesUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateRawDataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactPackagesUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_artifact_packages_update_annotations_error_component import (
            ApiV1ArtifactPackagesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_archived_at_error_component import (
            ApiV1ArtifactPackagesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_archived_by_error_component import (
            ApiV1ArtifactPackagesUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_archived_error_component import (
            ApiV1ArtifactPackagesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_archived_reason_error_component import (
            ApiV1ArtifactPackagesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_created_by_component_error_component import (
            ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_created_by_user_error_component import (
            ApiV1ArtifactPackagesUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_criticality_error_component import (
            ApiV1ArtifactPackagesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_debug_mode_error_component import (
            ApiV1ArtifactPackagesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_display_name_error_component import (
            ApiV1ArtifactPackagesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_kind_error_component import (
            ApiV1ArtifactPackagesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_labels_error_component import (
            ApiV1ArtifactPackagesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactPackagesUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_managed_by_content_type_error_component import (
            ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_managed_by_object_id_error_component import (
            ApiV1ArtifactPackagesUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_modified_by_user_error_component import (
            ApiV1ArtifactPackagesUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_name_error_component import (
            ApiV1ArtifactPackagesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_non_field_errors_error_component import (
            ApiV1ArtifactPackagesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactPackagesUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_platform_service_error_component import (
            ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_provider_error_component import (
            ApiV1ArtifactPackagesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_provider_id_error_component import (
            ApiV1ArtifactPackagesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_provider_reference_error_component import (
            ApiV1ArtifactPackagesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_raw_data_error_component import (
            ApiV1ArtifactPackagesUpdateRawDataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactPackagesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_sla_availability_error_component import (
            ApiV1ArtifactPackagesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_sla_target_error_component import (
            ApiV1ArtifactPackagesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_sla_window_days_error_component import (
            ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_slo_availability_error_component import (
            ApiV1ArtifactPackagesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_slo_target_error_component import (
            ApiV1ArtifactPackagesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_slo_window_days_error_component import (
            ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_target_availability_error_component import (
            ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_packages_update_tolerations_error_component import (
            ApiV1ArtifactPackagesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactPackagesUpdateAnnotationsErrorComponent
                | ApiV1ArtifactPackagesUpdateArchivedAtErrorComponent
                | ApiV1ArtifactPackagesUpdateArchivedByErrorComponent
                | ApiV1ArtifactPackagesUpdateArchivedErrorComponent
                | ApiV1ArtifactPackagesUpdateArchivedReasonErrorComponent
                | ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponent
                | ApiV1ArtifactPackagesUpdateCreatedByUserErrorComponent
                | ApiV1ArtifactPackagesUpdateCriticalityErrorComponent
                | ApiV1ArtifactPackagesUpdateDebugModeErrorComponent
                | ApiV1ArtifactPackagesUpdateDisplayNameErrorComponent
                | ApiV1ArtifactPackagesUpdateKindErrorComponent
                | ApiV1ArtifactPackagesUpdateLabelsErrorComponent
                | ApiV1ArtifactPackagesUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponent
                | ApiV1ArtifactPackagesUpdateManagedByObjectIdErrorComponent
                | ApiV1ArtifactPackagesUpdateModifiedByUserErrorComponent
                | ApiV1ArtifactPackagesUpdateNameErrorComponent
                | ApiV1ArtifactPackagesUpdateNonFieldErrorsErrorComponent
                | ApiV1ArtifactPackagesUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponent
                | ApiV1ArtifactPackagesUpdateProviderErrorComponent
                | ApiV1ArtifactPackagesUpdateProviderIdErrorComponent
                | ApiV1ArtifactPackagesUpdateProviderReferenceErrorComponent
                | ApiV1ArtifactPackagesUpdateRawDataErrorComponent
                | ApiV1ArtifactPackagesUpdateReconciliationEnabledErrorComponent
                | ApiV1ArtifactPackagesUpdateSlaAvailabilityErrorComponent
                | ApiV1ArtifactPackagesUpdateSlaTargetErrorComponent
                | ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponent
                | ApiV1ArtifactPackagesUpdateSloAvailabilityErrorComponent
                | ApiV1ArtifactPackagesUpdateSloTargetErrorComponent
                | ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponent
                | ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponent
                | ApiV1ArtifactPackagesUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_0 = (
                        ApiV1ArtifactPackagesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_1 = (
                        ApiV1ArtifactPackagesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_2 = (
                        ApiV1ArtifactPackagesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_3 = (
                        ApiV1ArtifactPackagesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_4 = (
                        ApiV1ArtifactPackagesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_5 = (
                        ApiV1ArtifactPackagesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_6 = (
                        ApiV1ArtifactPackagesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_7 = (
                        ApiV1ArtifactPackagesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_8 = (
                        ApiV1ArtifactPackagesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_9 = (
                        ApiV1ArtifactPackagesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_10 = (
                        ApiV1ArtifactPackagesUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_11 = (
                        ApiV1ArtifactPackagesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_12 = (
                        ApiV1ArtifactPackagesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_13 = (
                        ApiV1ArtifactPackagesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_14 = (
                        ApiV1ArtifactPackagesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_15 = (
                        ApiV1ArtifactPackagesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_16 = (
                        ApiV1ArtifactPackagesUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_17 = (
                        ApiV1ArtifactPackagesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_18 = (
                        ApiV1ArtifactPackagesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_19 = (
                        ApiV1ArtifactPackagesUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_20 = (
                        ApiV1ArtifactPackagesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_21 = (
                        ApiV1ArtifactPackagesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_22 = (
                        ApiV1ArtifactPackagesUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_23 = (
                        ApiV1ArtifactPackagesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_24 = (
                        ApiV1ArtifactPackagesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_25 = (
                        ApiV1ArtifactPackagesUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_26 = (
                        ApiV1ArtifactPackagesUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_27 = (
                        ApiV1ArtifactPackagesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_28 = (
                        ApiV1ArtifactPackagesUpdateRawDataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_29 = (
                        ApiV1ArtifactPackagesUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_30 = (
                        ApiV1ArtifactPackagesUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_packages_update_error_type_31 = (
                        ApiV1ArtifactPackagesUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_packages_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifact_packages_update_error_type_32 = (
                    ApiV1ArtifactPackagesUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifact_packages_update_error_type_32

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifact_packages_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifact_packages_update_validation_error.additional_properties = d
        return api_v1_artifact_packages_update_validation_error

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
