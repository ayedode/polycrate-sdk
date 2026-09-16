from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifact_repositories_archive_create_alternative_repository_url_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateAlternativeRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_annotations_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_archived_at_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_archived_by_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_archived_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_archived_reason_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_created_by_component_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_created_by_user_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_credential_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateCredentialErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_criticality_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_debug_mode_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_display_name_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_kind_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_labels_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_managed_by_content_type_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_managed_by_object_id_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_modified_by_user_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_name_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_non_field_errors_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_platform_dns_record_created_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_platform_service_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_provider_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_provider_id_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_provider_reference_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_reconciliation_enabled_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_repository_url_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_sla_availability_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_sla_target_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_sla_window_days_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_slo_availability_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_slo_target_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_slo_window_days_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_target_availability_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_archive_create_tolerations_error_component import (
        ApiV1ArtifactRepositoriesArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactRepositoriesArchiveCreateValidationError")


@_attrs_define
class ApiV1ArtifactRepositoriesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactRepositoriesArchiveCreateAlternativeRepositoryUrlErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateArchivedAtErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateArchivedReasonErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateCreatedByComponentErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateCreatedByUserErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateCredentialErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateDebugModeErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateKindErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreatePlatformServiceErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateProviderReferenceErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateSlaTargetErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateSloAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateSloTargetErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactRepositoriesArchiveCreateAlternativeRepositoryUrlErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateArchivedAtErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateArchivedReasonErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateCreatedByComponentErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateCreatedByUserErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateCredentialErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateDebugModeErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateKindErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreatePlatformServiceErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateProviderReferenceErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateSlaTargetErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateSloAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateSloTargetErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifact_repositories_archive_create_alternative_repository_url_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateAlternativeRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_annotations_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_archived_at_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_archived_by_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_archived_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_archived_reason_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_created_by_component_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_created_by_user_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_criticality_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_debug_mode_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_display_name_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_kind_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_labels_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_managed_by_content_type_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_managed_by_object_id_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_modified_by_user_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_name_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_non_field_errors_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_platform_service_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_provider_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_provider_id_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_provider_reference_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_repository_url_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_sla_availability_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_sla_target_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_sla_window_days_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_slo_availability_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_slo_target_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_slo_window_days_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_target_availability_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_tolerations_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactRepositoriesArchiveCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateAlternativeRepositoryUrlErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesArchiveCreateCreatedByUserErrorComponent):
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
        from ..models.api_v1_artifact_repositories_archive_create_alternative_repository_url_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateAlternativeRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_annotations_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_archived_at_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_archived_by_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_archived_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_archived_reason_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_created_by_component_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_created_by_user_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_credential_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_criticality_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_debug_mode_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_display_name_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_kind_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_labels_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_managed_by_content_type_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_managed_by_object_id_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_modified_by_user_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_name_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_non_field_errors_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_platform_dns_record_created_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_platform_service_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_provider_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_provider_id_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_provider_reference_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_reconciliation_enabled_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_repository_url_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_sla_availability_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_sla_target_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_sla_window_days_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_slo_availability_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_slo_target_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_slo_window_days_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_target_availability_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_archive_create_tolerations_error_component import (
            ApiV1ArtifactRepositoriesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactRepositoriesArchiveCreateAlternativeRepositoryUrlErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateArchivedAtErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateArchivedReasonErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateCreatedByComponentErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateCreatedByUserErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateCredentialErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateDebugModeErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateKindErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreatePlatformServiceErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateProviderReferenceErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateSlaTargetErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateSloAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateSloTargetErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_0 = (
                        ApiV1ArtifactRepositoriesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_1 = (
                        ApiV1ArtifactRepositoriesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_2 = (
                        ApiV1ArtifactRepositoriesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_3 = (
                        ApiV1ArtifactRepositoriesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_4 = (
                        ApiV1ArtifactRepositoriesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_5 = (
                        ApiV1ArtifactRepositoriesArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_6 = (
                        ApiV1ArtifactRepositoriesArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_7 = (
                        ApiV1ArtifactRepositoriesArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_8 = (
                        ApiV1ArtifactRepositoriesArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_9 = (
                        ApiV1ArtifactRepositoriesArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_10 = (
                        ApiV1ArtifactRepositoriesArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_11 = (
                        ApiV1ArtifactRepositoriesArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_12 = (
                        ApiV1ArtifactRepositoriesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_13 = (
                        ApiV1ArtifactRepositoriesArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_14 = (
                        ApiV1ArtifactRepositoriesArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_15 = (
                        ApiV1ArtifactRepositoriesArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_16 = (
                        ApiV1ArtifactRepositoriesArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_17 = (
                        ApiV1ArtifactRepositoriesArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_18 = (
                        ApiV1ArtifactRepositoriesArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_19 = (
                        ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_20 = (
                        ApiV1ArtifactRepositoriesArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_21 = (
                        ApiV1ArtifactRepositoriesArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_22 = (
                        ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_23 = (
                        ApiV1ArtifactRepositoriesArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_24 = (
                        ApiV1ArtifactRepositoriesArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_25 = (
                        ApiV1ArtifactRepositoriesArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_26 = (
                        ApiV1ArtifactRepositoriesArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_27 = (
                        ApiV1ArtifactRepositoriesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_28 = (
                        ApiV1ArtifactRepositoriesArchiveCreateRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_29 = (
                        ApiV1ArtifactRepositoriesArchiveCreateAlternativeRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_30 = (
                        ApiV1ArtifactRepositoriesArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_31 = (
                        ApiV1ArtifactRepositoriesArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_32 = (
                        ApiV1ArtifactRepositoriesArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_archive_create_error_type_33 = (
                        ApiV1ArtifactRepositoriesArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifact_repositories_archive_create_error_type_34 = (
                    ApiV1ArtifactRepositoriesArchiveCreateCredentialErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifact_repositories_archive_create_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifact_repositories_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifact_repositories_archive_create_validation_error.additional_properties = d
        return api_v1_artifact_repositories_archive_create_validation_error

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
