from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifact_repositories_create_alternative_repository_url_error_component import (
        ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_annotations_error_component import (
        ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_archived_at_error_component import (
        ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_archived_by_error_component import (
        ApiV1ArtifactRepositoriesCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_archived_error_component import (
        ApiV1ArtifactRepositoriesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_archived_reason_error_component import (
        ApiV1ArtifactRepositoriesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_created_by_component_error_component import (
        ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_created_by_user_error_component import (
        ApiV1ArtifactRepositoriesCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_credential_error_component import (
        ApiV1ArtifactRepositoriesCreateCredentialErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_criticality_error_component import (
        ApiV1ArtifactRepositoriesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_debug_mode_error_component import (
        ApiV1ArtifactRepositoriesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_display_name_error_component import (
        ApiV1ArtifactRepositoriesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_kind_error_component import (
        ApiV1ArtifactRepositoriesCreateKindErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_labels_error_component import (
        ApiV1ArtifactRepositoriesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_managed_by_content_type_error_component import (
        ApiV1ArtifactRepositoriesCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_managed_by_object_id_error_component import (
        ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_modified_by_user_error_component import (
        ApiV1ArtifactRepositoriesCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_name_error_component import (
        ApiV1ArtifactRepositoriesCreateNameErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_non_field_errors_error_component import (
        ApiV1ArtifactRepositoriesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_platform_dns_record_created_error_component import (
        ApiV1ArtifactRepositoriesCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_platform_service_error_component import (
        ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_provider_error_component import (
        ApiV1ArtifactRepositoriesCreateProviderErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_provider_id_error_component import (
        ApiV1ArtifactRepositoriesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_provider_reference_error_component import (
        ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_reconciliation_enabled_error_component import (
        ApiV1ArtifactRepositoriesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_repository_url_error_component import (
        ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_sla_availability_error_component import (
        ApiV1ArtifactRepositoriesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_sla_target_error_component import (
        ApiV1ArtifactRepositoriesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_sla_window_days_error_component import (
        ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_slo_availability_error_component import (
        ApiV1ArtifactRepositoriesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_slo_target_error_component import (
        ApiV1ArtifactRepositoriesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_slo_window_days_error_component import (
        ApiV1ArtifactRepositoriesCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_target_availability_error_component import (
        ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_create_tolerations_error_component import (
        ApiV1ArtifactRepositoriesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactRepositoriesCreateValidationError")


@_attrs_define
class ApiV1ArtifactRepositoriesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponent |
            ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponent |
            ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponent |
            ApiV1ArtifactRepositoriesCreateArchivedByErrorComponent | ApiV1ArtifactRepositoriesCreateArchivedErrorComponent
            | ApiV1ArtifactRepositoriesCreateArchivedReasonErrorComponent |
            ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponent |
            ApiV1ArtifactRepositoriesCreateCreatedByUserErrorComponent |
            ApiV1ArtifactRepositoriesCreateCredentialErrorComponent |
            ApiV1ArtifactRepositoriesCreateCriticalityErrorComponent |
            ApiV1ArtifactRepositoriesCreateDebugModeErrorComponent |
            ApiV1ArtifactRepositoriesCreateDisplayNameErrorComponent | ApiV1ArtifactRepositoriesCreateKindErrorComponent |
            ApiV1ArtifactRepositoriesCreateLabelsErrorComponent |
            ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ArtifactRepositoriesCreateManagedByContentTypeErrorComponent |
            ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponent |
            ApiV1ArtifactRepositoriesCreateModifiedByUserErrorComponent | ApiV1ArtifactRepositoriesCreateNameErrorComponent
            | ApiV1ArtifactRepositoriesCreateNonFieldErrorsErrorComponent |
            ApiV1ArtifactRepositoriesCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponent |
            ApiV1ArtifactRepositoriesCreateProviderErrorComponent | ApiV1ArtifactRepositoriesCreateProviderIdErrorComponent
            | ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponent |
            ApiV1ArtifactRepositoriesCreateReconciliationEnabledErrorComponent |
            ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponent |
            ApiV1ArtifactRepositoriesCreateSlaAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesCreateSlaTargetErrorComponent |
            ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponent |
            ApiV1ArtifactRepositoriesCreateSloAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesCreateSloTargetErrorComponent |
            ApiV1ArtifactRepositoriesCreateSloWindowDaysErrorComponent |
            ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponent
        | ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponent
        | ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponent
        | ApiV1ArtifactRepositoriesCreateArchivedByErrorComponent
        | ApiV1ArtifactRepositoriesCreateArchivedErrorComponent
        | ApiV1ArtifactRepositoriesCreateArchivedReasonErrorComponent
        | ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponent
        | ApiV1ArtifactRepositoriesCreateCreatedByUserErrorComponent
        | ApiV1ArtifactRepositoriesCreateCredentialErrorComponent
        | ApiV1ArtifactRepositoriesCreateCriticalityErrorComponent
        | ApiV1ArtifactRepositoriesCreateDebugModeErrorComponent
        | ApiV1ArtifactRepositoriesCreateDisplayNameErrorComponent
        | ApiV1ArtifactRepositoriesCreateKindErrorComponent
        | ApiV1ArtifactRepositoriesCreateLabelsErrorComponent
        | ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactRepositoriesCreateManagedByContentTypeErrorComponent
        | ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponent
        | ApiV1ArtifactRepositoriesCreateModifiedByUserErrorComponent
        | ApiV1ArtifactRepositoriesCreateNameErrorComponent
        | ApiV1ArtifactRepositoriesCreateNonFieldErrorsErrorComponent
        | ApiV1ArtifactRepositoriesCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponent
        | ApiV1ArtifactRepositoriesCreateProviderErrorComponent
        | ApiV1ArtifactRepositoriesCreateProviderIdErrorComponent
        | ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponent
        | ApiV1ArtifactRepositoriesCreateReconciliationEnabledErrorComponent
        | ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponent
        | ApiV1ArtifactRepositoriesCreateSlaAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesCreateSlaTargetErrorComponent
        | ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponent
        | ApiV1ArtifactRepositoriesCreateSloAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesCreateSloTargetErrorComponent
        | ApiV1ArtifactRepositoriesCreateSloWindowDaysErrorComponent
        | ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifact_repositories_create_alternative_repository_url_error_component import (
            ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_annotations_error_component import (
            ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_archived_at_error_component import (
            ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_archived_by_error_component import (
            ApiV1ArtifactRepositoriesCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_archived_error_component import (
            ApiV1ArtifactRepositoriesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_archived_reason_error_component import (
            ApiV1ArtifactRepositoriesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_created_by_component_error_component import (
            ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_created_by_user_error_component import (
            ApiV1ArtifactRepositoriesCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_criticality_error_component import (
            ApiV1ArtifactRepositoriesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_debug_mode_error_component import (
            ApiV1ArtifactRepositoriesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_display_name_error_component import (
            ApiV1ArtifactRepositoriesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_kind_error_component import (
            ApiV1ArtifactRepositoriesCreateKindErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_labels_error_component import (
            ApiV1ArtifactRepositoriesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_managed_by_content_type_error_component import (
            ApiV1ArtifactRepositoriesCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_managed_by_object_id_error_component import (
            ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_modified_by_user_error_component import (
            ApiV1ArtifactRepositoriesCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_name_error_component import (
            ApiV1ArtifactRepositoriesCreateNameErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_non_field_errors_error_component import (
            ApiV1ArtifactRepositoriesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactRepositoriesCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_platform_service_error_component import (
            ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_provider_error_component import (
            ApiV1ArtifactRepositoriesCreateProviderErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_provider_id_error_component import (
            ApiV1ArtifactRepositoriesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_provider_reference_error_component import (
            ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactRepositoriesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_repository_url_error_component import (
            ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_sla_availability_error_component import (
            ApiV1ArtifactRepositoriesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_sla_target_error_component import (
            ApiV1ArtifactRepositoriesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_sla_window_days_error_component import (
            ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_slo_availability_error_component import (
            ApiV1ArtifactRepositoriesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_slo_target_error_component import (
            ApiV1ArtifactRepositoriesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_slo_window_days_error_component import (
            ApiV1ArtifactRepositoriesCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_target_availability_error_component import (
            ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_tolerations_error_component import (
            ApiV1ArtifactRepositoriesCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesCreateCreatedByUserErrorComponent):
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
        from ..models.api_v1_artifact_repositories_create_alternative_repository_url_error_component import (
            ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_annotations_error_component import (
            ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_archived_at_error_component import (
            ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_archived_by_error_component import (
            ApiV1ArtifactRepositoriesCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_archived_error_component import (
            ApiV1ArtifactRepositoriesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_archived_reason_error_component import (
            ApiV1ArtifactRepositoriesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_created_by_component_error_component import (
            ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_created_by_user_error_component import (
            ApiV1ArtifactRepositoriesCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_credential_error_component import (
            ApiV1ArtifactRepositoriesCreateCredentialErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_criticality_error_component import (
            ApiV1ArtifactRepositoriesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_debug_mode_error_component import (
            ApiV1ArtifactRepositoriesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_display_name_error_component import (
            ApiV1ArtifactRepositoriesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_kind_error_component import (
            ApiV1ArtifactRepositoriesCreateKindErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_labels_error_component import (
            ApiV1ArtifactRepositoriesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_managed_by_content_type_error_component import (
            ApiV1ArtifactRepositoriesCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_managed_by_object_id_error_component import (
            ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_modified_by_user_error_component import (
            ApiV1ArtifactRepositoriesCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_name_error_component import (
            ApiV1ArtifactRepositoriesCreateNameErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_non_field_errors_error_component import (
            ApiV1ArtifactRepositoriesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactRepositoriesCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_platform_service_error_component import (
            ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_provider_error_component import (
            ApiV1ArtifactRepositoriesCreateProviderErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_provider_id_error_component import (
            ApiV1ArtifactRepositoriesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_provider_reference_error_component import (
            ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactRepositoriesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_repository_url_error_component import (
            ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_sla_availability_error_component import (
            ApiV1ArtifactRepositoriesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_sla_target_error_component import (
            ApiV1ArtifactRepositoriesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_sla_window_days_error_component import (
            ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_slo_availability_error_component import (
            ApiV1ArtifactRepositoriesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_slo_target_error_component import (
            ApiV1ArtifactRepositoriesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_slo_window_days_error_component import (
            ApiV1ArtifactRepositoriesCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_target_availability_error_component import (
            ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_artifact_repositories_create_tolerations_error_component import (
            ApiV1ArtifactRepositoriesCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponent
                | ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponent
                | ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponent
                | ApiV1ArtifactRepositoriesCreateArchivedByErrorComponent
                | ApiV1ArtifactRepositoriesCreateArchivedErrorComponent
                | ApiV1ArtifactRepositoriesCreateArchivedReasonErrorComponent
                | ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponent
                | ApiV1ArtifactRepositoriesCreateCreatedByUserErrorComponent
                | ApiV1ArtifactRepositoriesCreateCredentialErrorComponent
                | ApiV1ArtifactRepositoriesCreateCriticalityErrorComponent
                | ApiV1ArtifactRepositoriesCreateDebugModeErrorComponent
                | ApiV1ArtifactRepositoriesCreateDisplayNameErrorComponent
                | ApiV1ArtifactRepositoriesCreateKindErrorComponent
                | ApiV1ArtifactRepositoriesCreateLabelsErrorComponent
                | ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactRepositoriesCreateManagedByContentTypeErrorComponent
                | ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponent
                | ApiV1ArtifactRepositoriesCreateModifiedByUserErrorComponent
                | ApiV1ArtifactRepositoriesCreateNameErrorComponent
                | ApiV1ArtifactRepositoriesCreateNonFieldErrorsErrorComponent
                | ApiV1ArtifactRepositoriesCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponent
                | ApiV1ArtifactRepositoriesCreateProviderErrorComponent
                | ApiV1ArtifactRepositoriesCreateProviderIdErrorComponent
                | ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponent
                | ApiV1ArtifactRepositoriesCreateReconciliationEnabledErrorComponent
                | ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponent
                | ApiV1ArtifactRepositoriesCreateSlaAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesCreateSlaTargetErrorComponent
                | ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponent
                | ApiV1ArtifactRepositoriesCreateSloAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesCreateSloTargetErrorComponent
                | ApiV1ArtifactRepositoriesCreateSloWindowDaysErrorComponent
                | ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_0 = (
                        ApiV1ArtifactRepositoriesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_1 = (
                        ApiV1ArtifactRepositoriesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_2 = (
                        ApiV1ArtifactRepositoriesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_3 = (
                        ApiV1ArtifactRepositoriesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_4 = (
                        ApiV1ArtifactRepositoriesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_5 = (
                        ApiV1ArtifactRepositoriesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_6 = (
                        ApiV1ArtifactRepositoriesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_7 = (
                        ApiV1ArtifactRepositoriesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_8 = (
                        ApiV1ArtifactRepositoriesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_9 = (
                        ApiV1ArtifactRepositoriesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_10 = (
                        ApiV1ArtifactRepositoriesCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_11 = (
                        ApiV1ArtifactRepositoriesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_12 = (
                        ApiV1ArtifactRepositoriesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_13 = (
                        ApiV1ArtifactRepositoriesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_14 = (
                        ApiV1ArtifactRepositoriesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_15 = (
                        ApiV1ArtifactRepositoriesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_16 = (
                        ApiV1ArtifactRepositoriesCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_17 = (
                        ApiV1ArtifactRepositoriesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_18 = (
                        ApiV1ArtifactRepositoriesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_19 = (
                        ApiV1ArtifactRepositoriesCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_20 = (
                        ApiV1ArtifactRepositoriesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_21 = (
                        ApiV1ArtifactRepositoriesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_22 = (
                        ApiV1ArtifactRepositoriesCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_23 = (
                        ApiV1ArtifactRepositoriesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_24 = (
                        ApiV1ArtifactRepositoriesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_25 = (
                        ApiV1ArtifactRepositoriesCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_26 = (
                        ApiV1ArtifactRepositoriesCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_27 = (
                        ApiV1ArtifactRepositoriesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_28 = (
                        ApiV1ArtifactRepositoriesCreateRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_29 = (
                        ApiV1ArtifactRepositoriesCreateAlternativeRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_30 = (
                        ApiV1ArtifactRepositoriesCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_31 = (
                        ApiV1ArtifactRepositoriesCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_32 = (
                        ApiV1ArtifactRepositoriesCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_create_error_type_33 = (
                        ApiV1ArtifactRepositoriesCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifact_repositories_create_error_type_34 = (
                    ApiV1ArtifactRepositoriesCreateCredentialErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifact_repositories_create_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifact_repositories_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifact_repositories_create_validation_error.additional_properties = d
        return api_v1_artifact_repositories_create_validation_error

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
