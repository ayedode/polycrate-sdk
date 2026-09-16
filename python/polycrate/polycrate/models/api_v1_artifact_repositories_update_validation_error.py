from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_artifact_repositories_update_alternative_repository_url_error_component import (
        ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_annotations_error_component import (
        ApiV1ArtifactRepositoriesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_archived_at_error_component import (
        ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_archived_by_error_component import (
        ApiV1ArtifactRepositoriesUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_archived_error_component import (
        ApiV1ArtifactRepositoriesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_archived_reason_error_component import (
        ApiV1ArtifactRepositoriesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_created_by_component_error_component import (
        ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_created_by_user_error_component import (
        ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_credential_error_component import (
        ApiV1ArtifactRepositoriesUpdateCredentialErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_criticality_error_component import (
        ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_debug_mode_error_component import (
        ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_display_name_error_component import (
        ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_kind_error_component import (
        ApiV1ArtifactRepositoriesUpdateKindErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_labels_error_component import (
        ApiV1ArtifactRepositoriesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_managed_by_content_type_error_component import (
        ApiV1ArtifactRepositoriesUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_managed_by_object_id_error_component import (
        ApiV1ArtifactRepositoriesUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_modified_by_user_error_component import (
        ApiV1ArtifactRepositoriesUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_name_error_component import (
        ApiV1ArtifactRepositoriesUpdateNameErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_non_field_errors_error_component import (
        ApiV1ArtifactRepositoriesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_platform_dns_record_created_error_component import (
        ApiV1ArtifactRepositoriesUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_platform_service_error_component import (
        ApiV1ArtifactRepositoriesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_provider_error_component import (
        ApiV1ArtifactRepositoriesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_provider_id_error_component import (
        ApiV1ArtifactRepositoriesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_provider_reference_error_component import (
        ApiV1ArtifactRepositoriesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_reconciliation_enabled_error_component import (
        ApiV1ArtifactRepositoriesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_repository_url_error_component import (
        ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_sla_availability_error_component import (
        ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_sla_target_error_component import (
        ApiV1ArtifactRepositoriesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_sla_window_days_error_component import (
        ApiV1ArtifactRepositoriesUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_slo_availability_error_component import (
        ApiV1ArtifactRepositoriesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_slo_target_error_component import (
        ApiV1ArtifactRepositoriesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_slo_window_days_error_component import (
        ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_target_availability_error_component import (
        ApiV1ArtifactRepositoriesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_artifact_repositories_update_tolerations_error_component import (
        ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ArtifactRepositoriesUpdateValidationError")


@_attrs_define
class ApiV1ArtifactRepositoriesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponent |
            ApiV1ArtifactRepositoriesUpdateAnnotationsErrorComponent |
            ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponent |
            ApiV1ArtifactRepositoriesUpdateArchivedByErrorComponent | ApiV1ArtifactRepositoriesUpdateArchivedErrorComponent
            | ApiV1ArtifactRepositoriesUpdateArchivedReasonErrorComponent |
            ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponent |
            ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponent |
            ApiV1ArtifactRepositoriesUpdateCredentialErrorComponent |
            ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponent |
            ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponent |
            ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponent | ApiV1ArtifactRepositoriesUpdateKindErrorComponent |
            ApiV1ArtifactRepositoriesUpdateLabelsErrorComponent |
            ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ArtifactRepositoriesUpdateManagedByContentTypeErrorComponent |
            ApiV1ArtifactRepositoriesUpdateManagedByObjectIdErrorComponent |
            ApiV1ArtifactRepositoriesUpdateModifiedByUserErrorComponent | ApiV1ArtifactRepositoriesUpdateNameErrorComponent
            | ApiV1ArtifactRepositoriesUpdateNonFieldErrorsErrorComponent |
            ApiV1ArtifactRepositoriesUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ArtifactRepositoriesUpdatePlatformServiceErrorComponent |
            ApiV1ArtifactRepositoriesUpdateProviderErrorComponent | ApiV1ArtifactRepositoriesUpdateProviderIdErrorComponent
            | ApiV1ArtifactRepositoriesUpdateProviderReferenceErrorComponent |
            ApiV1ArtifactRepositoriesUpdateReconciliationEnabledErrorComponent |
            ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponent |
            ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesUpdateSlaTargetErrorComponent |
            ApiV1ArtifactRepositoriesUpdateSlaWindowDaysErrorComponent |
            ApiV1ArtifactRepositoriesUpdateSloAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesUpdateSloTargetErrorComponent |
            ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponent |
            ApiV1ArtifactRepositoriesUpdateTargetAvailabilityErrorComponent |
            ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponent
        | ApiV1ArtifactRepositoriesUpdateAnnotationsErrorComponent
        | ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponent
        | ApiV1ArtifactRepositoriesUpdateArchivedByErrorComponent
        | ApiV1ArtifactRepositoriesUpdateArchivedErrorComponent
        | ApiV1ArtifactRepositoriesUpdateArchivedReasonErrorComponent
        | ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponent
        | ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponent
        | ApiV1ArtifactRepositoriesUpdateCredentialErrorComponent
        | ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponent
        | ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponent
        | ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponent
        | ApiV1ArtifactRepositoriesUpdateKindErrorComponent
        | ApiV1ArtifactRepositoriesUpdateLabelsErrorComponent
        | ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ArtifactRepositoriesUpdateManagedByContentTypeErrorComponent
        | ApiV1ArtifactRepositoriesUpdateManagedByObjectIdErrorComponent
        | ApiV1ArtifactRepositoriesUpdateModifiedByUserErrorComponent
        | ApiV1ArtifactRepositoriesUpdateNameErrorComponent
        | ApiV1ArtifactRepositoriesUpdateNonFieldErrorsErrorComponent
        | ApiV1ArtifactRepositoriesUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ArtifactRepositoriesUpdatePlatformServiceErrorComponent
        | ApiV1ArtifactRepositoriesUpdateProviderErrorComponent
        | ApiV1ArtifactRepositoriesUpdateProviderIdErrorComponent
        | ApiV1ArtifactRepositoriesUpdateProviderReferenceErrorComponent
        | ApiV1ArtifactRepositoriesUpdateReconciliationEnabledErrorComponent
        | ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponent
        | ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesUpdateSlaTargetErrorComponent
        | ApiV1ArtifactRepositoriesUpdateSlaWindowDaysErrorComponent
        | ApiV1ArtifactRepositoriesUpdateSloAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesUpdateSloTargetErrorComponent
        | ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponent
        | ApiV1ArtifactRepositoriesUpdateTargetAvailabilityErrorComponent
        | ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_artifact_repositories_update_alternative_repository_url_error_component import (
            ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_annotations_error_component import (
            ApiV1ArtifactRepositoriesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_archived_at_error_component import (
            ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_archived_by_error_component import (
            ApiV1ArtifactRepositoriesUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_archived_error_component import (
            ApiV1ArtifactRepositoriesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_archived_reason_error_component import (
            ApiV1ArtifactRepositoriesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_created_by_component_error_component import (
            ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_created_by_user_error_component import (
            ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_criticality_error_component import (
            ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_debug_mode_error_component import (
            ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_display_name_error_component import (
            ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_kind_error_component import (
            ApiV1ArtifactRepositoriesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_labels_error_component import (
            ApiV1ArtifactRepositoriesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_managed_by_content_type_error_component import (
            ApiV1ArtifactRepositoriesUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_managed_by_object_id_error_component import (
            ApiV1ArtifactRepositoriesUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_modified_by_user_error_component import (
            ApiV1ArtifactRepositoriesUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_name_error_component import (
            ApiV1ArtifactRepositoriesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_non_field_errors_error_component import (
            ApiV1ArtifactRepositoriesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactRepositoriesUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_platform_service_error_component import (
            ApiV1ArtifactRepositoriesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_provider_error_component import (
            ApiV1ArtifactRepositoriesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_provider_id_error_component import (
            ApiV1ArtifactRepositoriesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_provider_reference_error_component import (
            ApiV1ArtifactRepositoriesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactRepositoriesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_repository_url_error_component import (
            ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_sla_availability_error_component import (
            ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_sla_target_error_component import (
            ApiV1ArtifactRepositoriesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_sla_window_days_error_component import (
            ApiV1ArtifactRepositoriesUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_slo_availability_error_component import (
            ApiV1ArtifactRepositoriesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_slo_target_error_component import (
            ApiV1ArtifactRepositoriesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_slo_window_days_error_component import (
            ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_target_availability_error_component import (
            ApiV1ArtifactRepositoriesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_tolerations_error_component import (
            ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponent):
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
        from ..models.api_v1_artifact_repositories_update_alternative_repository_url_error_component import (
            ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_annotations_error_component import (
            ApiV1ArtifactRepositoriesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_archived_at_error_component import (
            ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_archived_by_error_component import (
            ApiV1ArtifactRepositoriesUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_archived_error_component import (
            ApiV1ArtifactRepositoriesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_archived_reason_error_component import (
            ApiV1ArtifactRepositoriesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_created_by_component_error_component import (
            ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_created_by_user_error_component import (
            ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_credential_error_component import (
            ApiV1ArtifactRepositoriesUpdateCredentialErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_criticality_error_component import (
            ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_debug_mode_error_component import (
            ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_display_name_error_component import (
            ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_kind_error_component import (
            ApiV1ArtifactRepositoriesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_labels_error_component import (
            ApiV1ArtifactRepositoriesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_managed_by_content_type_error_component import (
            ApiV1ArtifactRepositoriesUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_managed_by_object_id_error_component import (
            ApiV1ArtifactRepositoriesUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_modified_by_user_error_component import (
            ApiV1ArtifactRepositoriesUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_name_error_component import (
            ApiV1ArtifactRepositoriesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_non_field_errors_error_component import (
            ApiV1ArtifactRepositoriesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_platform_dns_record_created_error_component import (
            ApiV1ArtifactRepositoriesUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_platform_service_error_component import (
            ApiV1ArtifactRepositoriesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_provider_error_component import (
            ApiV1ArtifactRepositoriesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_provider_id_error_component import (
            ApiV1ArtifactRepositoriesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_provider_reference_error_component import (
            ApiV1ArtifactRepositoriesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_reconciliation_enabled_error_component import (
            ApiV1ArtifactRepositoriesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_repository_url_error_component import (
            ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_sla_availability_error_component import (
            ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_sla_target_error_component import (
            ApiV1ArtifactRepositoriesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_sla_window_days_error_component import (
            ApiV1ArtifactRepositoriesUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_slo_availability_error_component import (
            ApiV1ArtifactRepositoriesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_slo_target_error_component import (
            ApiV1ArtifactRepositoriesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_slo_window_days_error_component import (
            ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_target_availability_error_component import (
            ApiV1ArtifactRepositoriesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_artifact_repositories_update_tolerations_error_component import (
            ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponent
                | ApiV1ArtifactRepositoriesUpdateAnnotationsErrorComponent
                | ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponent
                | ApiV1ArtifactRepositoriesUpdateArchivedByErrorComponent
                | ApiV1ArtifactRepositoriesUpdateArchivedErrorComponent
                | ApiV1ArtifactRepositoriesUpdateArchivedReasonErrorComponent
                | ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponent
                | ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponent
                | ApiV1ArtifactRepositoriesUpdateCredentialErrorComponent
                | ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponent
                | ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponent
                | ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponent
                | ApiV1ArtifactRepositoriesUpdateKindErrorComponent
                | ApiV1ArtifactRepositoriesUpdateLabelsErrorComponent
                | ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ArtifactRepositoriesUpdateManagedByContentTypeErrorComponent
                | ApiV1ArtifactRepositoriesUpdateManagedByObjectIdErrorComponent
                | ApiV1ArtifactRepositoriesUpdateModifiedByUserErrorComponent
                | ApiV1ArtifactRepositoriesUpdateNameErrorComponent
                | ApiV1ArtifactRepositoriesUpdateNonFieldErrorsErrorComponent
                | ApiV1ArtifactRepositoriesUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ArtifactRepositoriesUpdatePlatformServiceErrorComponent
                | ApiV1ArtifactRepositoriesUpdateProviderErrorComponent
                | ApiV1ArtifactRepositoriesUpdateProviderIdErrorComponent
                | ApiV1ArtifactRepositoriesUpdateProviderReferenceErrorComponent
                | ApiV1ArtifactRepositoriesUpdateReconciliationEnabledErrorComponent
                | ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponent
                | ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesUpdateSlaTargetErrorComponent
                | ApiV1ArtifactRepositoriesUpdateSlaWindowDaysErrorComponent
                | ApiV1ArtifactRepositoriesUpdateSloAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesUpdateSloTargetErrorComponent
                | ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponent
                | ApiV1ArtifactRepositoriesUpdateTargetAvailabilityErrorComponent
                | ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_0 = (
                        ApiV1ArtifactRepositoriesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_1 = (
                        ApiV1ArtifactRepositoriesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_2 = (
                        ApiV1ArtifactRepositoriesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_3 = (
                        ApiV1ArtifactRepositoriesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_4 = (
                        ApiV1ArtifactRepositoriesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_5 = (
                        ApiV1ArtifactRepositoriesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_6 = (
                        ApiV1ArtifactRepositoriesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_7 = (
                        ApiV1ArtifactRepositoriesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_8 = (
                        ApiV1ArtifactRepositoriesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_9 = (
                        ApiV1ArtifactRepositoriesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_10 = (
                        ApiV1ArtifactRepositoriesUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_11 = (
                        ApiV1ArtifactRepositoriesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_12 = (
                        ApiV1ArtifactRepositoriesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_13 = (
                        ApiV1ArtifactRepositoriesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_14 = (
                        ApiV1ArtifactRepositoriesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_15 = (
                        ApiV1ArtifactRepositoriesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_16 = (
                        ApiV1ArtifactRepositoriesUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_17 = (
                        ApiV1ArtifactRepositoriesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_18 = (
                        ApiV1ArtifactRepositoriesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_19 = (
                        ApiV1ArtifactRepositoriesUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_20 = (
                        ApiV1ArtifactRepositoriesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_21 = (
                        ApiV1ArtifactRepositoriesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_22 = (
                        ApiV1ArtifactRepositoriesUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_23 = (
                        ApiV1ArtifactRepositoriesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_24 = (
                        ApiV1ArtifactRepositoriesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_25 = (
                        ApiV1ArtifactRepositoriesUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_26 = (
                        ApiV1ArtifactRepositoriesUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_27 = (
                        ApiV1ArtifactRepositoriesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_28 = (
                        ApiV1ArtifactRepositoriesUpdateRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_29 = (
                        ApiV1ArtifactRepositoriesUpdateAlternativeRepositoryUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_30 = (
                        ApiV1ArtifactRepositoriesUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_31 = (
                        ApiV1ArtifactRepositoriesUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_32 = (
                        ApiV1ArtifactRepositoriesUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_artifact_repositories_update_error_type_33 = (
                        ApiV1ArtifactRepositoriesUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_artifact_repositories_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_artifact_repositories_update_error_type_34 = (
                    ApiV1ArtifactRepositoriesUpdateCredentialErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_artifact_repositories_update_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_artifact_repositories_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_artifact_repositories_update_validation_error.additional_properties = d
        return api_v1_artifact_repositories_update_validation_error

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
