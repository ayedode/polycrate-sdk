from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_provider_accounts_update_annotations_error_component import (
        ApiV1ProviderAccountsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_api_backoff_minutes_error_component import (
        ApiV1ProviderAccountsUpdateApiBackoffMinutesErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_api_endpoint_error_component import (
        ApiV1ProviderAccountsUpdateApiEndpointErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_api_kind_error_component import (
        ApiV1ProviderAccountsUpdateApiKindErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_archived_at_error_component import (
        ApiV1ProviderAccountsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_archived_by_error_component import (
        ApiV1ProviderAccountsUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_archived_error_component import (
        ApiV1ProviderAccountsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_archived_reason_error_component import (
        ApiV1ProviderAccountsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_created_by_component_error_component import (
        ApiV1ProviderAccountsUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_created_by_user_error_component import (
        ApiV1ProviderAccountsUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_credential_id_error_component import (
        ApiV1ProviderAccountsUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_criticality_error_component import (
        ApiV1ProviderAccountsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_debug_mode_error_component import (
        ApiV1ProviderAccountsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_display_name_error_component import (
        ApiV1ProviderAccountsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_kind_error_component import (
        ApiV1ProviderAccountsUpdateKindErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_labels_error_component import (
        ApiV1ProviderAccountsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_last_rate_limited_at_error_component import (
        ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1ProviderAccountsUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_managed_by_content_type_error_component import (
        ApiV1ProviderAccountsUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_managed_by_object_id_error_component import (
        ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_metadata_error_component import (
        ApiV1ProviderAccountsUpdateMetadataErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_modified_by_user_error_component import (
        ApiV1ProviderAccountsUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_name_error_component import (
        ApiV1ProviderAccountsUpdateNameErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_non_field_errors_error_component import (
        ApiV1ProviderAccountsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_organization_id_error_component import (
        ApiV1ProviderAccountsUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_platform_dns_record_created_error_component import (
        ApiV1ProviderAccountsUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_platform_service_error_component import (
        ApiV1ProviderAccountsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_provider_entity_id_error_component import (
        ApiV1ProviderAccountsUpdateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_provider_error_component import (
        ApiV1ProviderAccountsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_provider_id_error_component import (
        ApiV1ProviderAccountsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_provider_reference_error_component import (
        ApiV1ProviderAccountsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_reconciliation_enabled_error_component import (
        ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_sla_availability_error_component import (
        ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_sla_target_error_component import (
        ApiV1ProviderAccountsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_sla_window_days_error_component import (
        ApiV1ProviderAccountsUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_slo_availability_error_component import (
        ApiV1ProviderAccountsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_slo_target_error_component import (
        ApiV1ProviderAccountsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_slo_window_days_error_component import (
        ApiV1ProviderAccountsUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_target_availability_error_component import (
        ApiV1ProviderAccountsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_tolerations_error_component import (
        ApiV1ProviderAccountsUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_provider_accounts_update_workspace_id_error_component import (
        ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProviderAccountsUpdateValidationError")


@_attrs_define
class ApiV1ProviderAccountsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProviderAccountsUpdateAnnotationsErrorComponent |
            ApiV1ProviderAccountsUpdateApiBackoffMinutesErrorComponent |
            ApiV1ProviderAccountsUpdateApiEndpointErrorComponent | ApiV1ProviderAccountsUpdateApiKindErrorComponent |
            ApiV1ProviderAccountsUpdateArchivedAtErrorComponent | ApiV1ProviderAccountsUpdateArchivedByErrorComponent |
            ApiV1ProviderAccountsUpdateArchivedErrorComponent | ApiV1ProviderAccountsUpdateArchivedReasonErrorComponent |
            ApiV1ProviderAccountsUpdateCreatedByComponentErrorComponent |
            ApiV1ProviderAccountsUpdateCreatedByUserErrorComponent | ApiV1ProviderAccountsUpdateCredentialIdErrorComponent |
            ApiV1ProviderAccountsUpdateCriticalityErrorComponent | ApiV1ProviderAccountsUpdateDebugModeErrorComponent |
            ApiV1ProviderAccountsUpdateDisplayNameErrorComponent | ApiV1ProviderAccountsUpdateKindErrorComponent |
            ApiV1ProviderAccountsUpdateLabelsErrorComponent | ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponent |
            ApiV1ProviderAccountsUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1ProviderAccountsUpdateManagedByContentTypeErrorComponent |
            ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponent | ApiV1ProviderAccountsUpdateMetadataErrorComponent |
            ApiV1ProviderAccountsUpdateModifiedByUserErrorComponent | ApiV1ProviderAccountsUpdateNameErrorComponent |
            ApiV1ProviderAccountsUpdateNonFieldErrorsErrorComponent |
            ApiV1ProviderAccountsUpdateOrganizationIdErrorComponent |
            ApiV1ProviderAccountsUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1ProviderAccountsUpdatePlatformServiceErrorComponent |
            ApiV1ProviderAccountsUpdateProviderEntityIdErrorComponent | ApiV1ProviderAccountsUpdateProviderErrorComponent |
            ApiV1ProviderAccountsUpdateProviderIdErrorComponent | ApiV1ProviderAccountsUpdateProviderReferenceErrorComponent
            | ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponent |
            ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponent | ApiV1ProviderAccountsUpdateSlaTargetErrorComponent |
            ApiV1ProviderAccountsUpdateSlaWindowDaysErrorComponent |
            ApiV1ProviderAccountsUpdateSloAvailabilityErrorComponent | ApiV1ProviderAccountsUpdateSloTargetErrorComponent |
            ApiV1ProviderAccountsUpdateSloWindowDaysErrorComponent |
            ApiV1ProviderAccountsUpdateTargetAvailabilityErrorComponent |
            ApiV1ProviderAccountsUpdateTolerationsErrorComponent | ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProviderAccountsUpdateAnnotationsErrorComponent
        | ApiV1ProviderAccountsUpdateApiBackoffMinutesErrorComponent
        | ApiV1ProviderAccountsUpdateApiEndpointErrorComponent
        | ApiV1ProviderAccountsUpdateApiKindErrorComponent
        | ApiV1ProviderAccountsUpdateArchivedAtErrorComponent
        | ApiV1ProviderAccountsUpdateArchivedByErrorComponent
        | ApiV1ProviderAccountsUpdateArchivedErrorComponent
        | ApiV1ProviderAccountsUpdateArchivedReasonErrorComponent
        | ApiV1ProviderAccountsUpdateCreatedByComponentErrorComponent
        | ApiV1ProviderAccountsUpdateCreatedByUserErrorComponent
        | ApiV1ProviderAccountsUpdateCredentialIdErrorComponent
        | ApiV1ProviderAccountsUpdateCriticalityErrorComponent
        | ApiV1ProviderAccountsUpdateDebugModeErrorComponent
        | ApiV1ProviderAccountsUpdateDisplayNameErrorComponent
        | ApiV1ProviderAccountsUpdateKindErrorComponent
        | ApiV1ProviderAccountsUpdateLabelsErrorComponent
        | ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponent
        | ApiV1ProviderAccountsUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1ProviderAccountsUpdateManagedByContentTypeErrorComponent
        | ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponent
        | ApiV1ProviderAccountsUpdateMetadataErrorComponent
        | ApiV1ProviderAccountsUpdateModifiedByUserErrorComponent
        | ApiV1ProviderAccountsUpdateNameErrorComponent
        | ApiV1ProviderAccountsUpdateNonFieldErrorsErrorComponent
        | ApiV1ProviderAccountsUpdateOrganizationIdErrorComponent
        | ApiV1ProviderAccountsUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1ProviderAccountsUpdatePlatformServiceErrorComponent
        | ApiV1ProviderAccountsUpdateProviderEntityIdErrorComponent
        | ApiV1ProviderAccountsUpdateProviderErrorComponent
        | ApiV1ProviderAccountsUpdateProviderIdErrorComponent
        | ApiV1ProviderAccountsUpdateProviderReferenceErrorComponent
        | ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponent
        | ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponent
        | ApiV1ProviderAccountsUpdateSlaTargetErrorComponent
        | ApiV1ProviderAccountsUpdateSlaWindowDaysErrorComponent
        | ApiV1ProviderAccountsUpdateSloAvailabilityErrorComponent
        | ApiV1ProviderAccountsUpdateSloTargetErrorComponent
        | ApiV1ProviderAccountsUpdateSloWindowDaysErrorComponent
        | ApiV1ProviderAccountsUpdateTargetAvailabilityErrorComponent
        | ApiV1ProviderAccountsUpdateTolerationsErrorComponent
        | ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_provider_accounts_update_annotations_error_component import (
            ApiV1ProviderAccountsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_api_backoff_minutes_error_component import (
            ApiV1ProviderAccountsUpdateApiBackoffMinutesErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_api_endpoint_error_component import (
            ApiV1ProviderAccountsUpdateApiEndpointErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_api_kind_error_component import (
            ApiV1ProviderAccountsUpdateApiKindErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_archived_at_error_component import (
            ApiV1ProviderAccountsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_archived_by_error_component import (
            ApiV1ProviderAccountsUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_archived_error_component import (
            ApiV1ProviderAccountsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_archived_reason_error_component import (
            ApiV1ProviderAccountsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_created_by_component_error_component import (
            ApiV1ProviderAccountsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_credential_id_error_component import (
            ApiV1ProviderAccountsUpdateCredentialIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_criticality_error_component import (
            ApiV1ProviderAccountsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_debug_mode_error_component import (
            ApiV1ProviderAccountsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_display_name_error_component import (
            ApiV1ProviderAccountsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_kind_error_component import (
            ApiV1ProviderAccountsUpdateKindErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_labels_error_component import (
            ApiV1ProviderAccountsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_last_rate_limited_at_error_component import (
            ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ProviderAccountsUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_managed_by_content_type_error_component import (
            ApiV1ProviderAccountsUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_managed_by_object_id_error_component import (
            ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_metadata_error_component import (
            ApiV1ProviderAccountsUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_modified_by_user_error_component import (
            ApiV1ProviderAccountsUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_name_error_component import (
            ApiV1ProviderAccountsUpdateNameErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_non_field_errors_error_component import (
            ApiV1ProviderAccountsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_organization_id_error_component import (
            ApiV1ProviderAccountsUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_platform_dns_record_created_error_component import (
            ApiV1ProviderAccountsUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_platform_service_error_component import (
            ApiV1ProviderAccountsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_provider_entity_id_error_component import (
            ApiV1ProviderAccountsUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_provider_error_component import (
            ApiV1ProviderAccountsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_provider_id_error_component import (
            ApiV1ProviderAccountsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_provider_reference_error_component import (
            ApiV1ProviderAccountsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_reconciliation_enabled_error_component import (
            ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_sla_availability_error_component import (
            ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_sla_target_error_component import (
            ApiV1ProviderAccountsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_sla_window_days_error_component import (
            ApiV1ProviderAccountsUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_slo_availability_error_component import (
            ApiV1ProviderAccountsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_slo_target_error_component import (
            ApiV1ProviderAccountsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_slo_window_days_error_component import (
            ApiV1ProviderAccountsUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_target_availability_error_component import (
            ApiV1ProviderAccountsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_tolerations_error_component import (
            ApiV1ProviderAccountsUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_workspace_id_error_component import (
            ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProviderAccountsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateProviderEntityIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1ProviderAccountsUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateApiKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateApiEndpointErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateApiBackoffMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProviderAccountsUpdateModifiedByUserErrorComponent):
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
        from ..models.api_v1_provider_accounts_update_annotations_error_component import (
            ApiV1ProviderAccountsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_api_backoff_minutes_error_component import (
            ApiV1ProviderAccountsUpdateApiBackoffMinutesErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_api_endpoint_error_component import (
            ApiV1ProviderAccountsUpdateApiEndpointErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_api_kind_error_component import (
            ApiV1ProviderAccountsUpdateApiKindErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_archived_at_error_component import (
            ApiV1ProviderAccountsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_archived_by_error_component import (
            ApiV1ProviderAccountsUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_archived_error_component import (
            ApiV1ProviderAccountsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_archived_reason_error_component import (
            ApiV1ProviderAccountsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_created_by_component_error_component import (
            ApiV1ProviderAccountsUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_created_by_user_error_component import (
            ApiV1ProviderAccountsUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_credential_id_error_component import (
            ApiV1ProviderAccountsUpdateCredentialIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_criticality_error_component import (
            ApiV1ProviderAccountsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_debug_mode_error_component import (
            ApiV1ProviderAccountsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_display_name_error_component import (
            ApiV1ProviderAccountsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_kind_error_component import (
            ApiV1ProviderAccountsUpdateKindErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_labels_error_component import (
            ApiV1ProviderAccountsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_last_rate_limited_at_error_component import (
            ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1ProviderAccountsUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_managed_by_content_type_error_component import (
            ApiV1ProviderAccountsUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_managed_by_object_id_error_component import (
            ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_metadata_error_component import (
            ApiV1ProviderAccountsUpdateMetadataErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_modified_by_user_error_component import (
            ApiV1ProviderAccountsUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_name_error_component import (
            ApiV1ProviderAccountsUpdateNameErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_non_field_errors_error_component import (
            ApiV1ProviderAccountsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_organization_id_error_component import (
            ApiV1ProviderAccountsUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_platform_dns_record_created_error_component import (
            ApiV1ProviderAccountsUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_platform_service_error_component import (
            ApiV1ProviderAccountsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_provider_entity_id_error_component import (
            ApiV1ProviderAccountsUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_provider_error_component import (
            ApiV1ProviderAccountsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_provider_id_error_component import (
            ApiV1ProviderAccountsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_provider_reference_error_component import (
            ApiV1ProviderAccountsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_reconciliation_enabled_error_component import (
            ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_sla_availability_error_component import (
            ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_sla_target_error_component import (
            ApiV1ProviderAccountsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_sla_window_days_error_component import (
            ApiV1ProviderAccountsUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_slo_availability_error_component import (
            ApiV1ProviderAccountsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_slo_target_error_component import (
            ApiV1ProviderAccountsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_slo_window_days_error_component import (
            ApiV1ProviderAccountsUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_target_availability_error_component import (
            ApiV1ProviderAccountsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_tolerations_error_component import (
            ApiV1ProviderAccountsUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_provider_accounts_update_workspace_id_error_component import (
            ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProviderAccountsUpdateAnnotationsErrorComponent
                | ApiV1ProviderAccountsUpdateApiBackoffMinutesErrorComponent
                | ApiV1ProviderAccountsUpdateApiEndpointErrorComponent
                | ApiV1ProviderAccountsUpdateApiKindErrorComponent
                | ApiV1ProviderAccountsUpdateArchivedAtErrorComponent
                | ApiV1ProviderAccountsUpdateArchivedByErrorComponent
                | ApiV1ProviderAccountsUpdateArchivedErrorComponent
                | ApiV1ProviderAccountsUpdateArchivedReasonErrorComponent
                | ApiV1ProviderAccountsUpdateCreatedByComponentErrorComponent
                | ApiV1ProviderAccountsUpdateCreatedByUserErrorComponent
                | ApiV1ProviderAccountsUpdateCredentialIdErrorComponent
                | ApiV1ProviderAccountsUpdateCriticalityErrorComponent
                | ApiV1ProviderAccountsUpdateDebugModeErrorComponent
                | ApiV1ProviderAccountsUpdateDisplayNameErrorComponent
                | ApiV1ProviderAccountsUpdateKindErrorComponent
                | ApiV1ProviderAccountsUpdateLabelsErrorComponent
                | ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponent
                | ApiV1ProviderAccountsUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1ProviderAccountsUpdateManagedByContentTypeErrorComponent
                | ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponent
                | ApiV1ProviderAccountsUpdateMetadataErrorComponent
                | ApiV1ProviderAccountsUpdateModifiedByUserErrorComponent
                | ApiV1ProviderAccountsUpdateNameErrorComponent
                | ApiV1ProviderAccountsUpdateNonFieldErrorsErrorComponent
                | ApiV1ProviderAccountsUpdateOrganizationIdErrorComponent
                | ApiV1ProviderAccountsUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1ProviderAccountsUpdatePlatformServiceErrorComponent
                | ApiV1ProviderAccountsUpdateProviderEntityIdErrorComponent
                | ApiV1ProviderAccountsUpdateProviderErrorComponent
                | ApiV1ProviderAccountsUpdateProviderIdErrorComponent
                | ApiV1ProviderAccountsUpdateProviderReferenceErrorComponent
                | ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponent
                | ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponent
                | ApiV1ProviderAccountsUpdateSlaTargetErrorComponent
                | ApiV1ProviderAccountsUpdateSlaWindowDaysErrorComponent
                | ApiV1ProviderAccountsUpdateSloAvailabilityErrorComponent
                | ApiV1ProviderAccountsUpdateSloTargetErrorComponent
                | ApiV1ProviderAccountsUpdateSloWindowDaysErrorComponent
                | ApiV1ProviderAccountsUpdateTargetAvailabilityErrorComponent
                | ApiV1ProviderAccountsUpdateTolerationsErrorComponent
                | ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_0 = (
                        ApiV1ProviderAccountsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_1 = (
                        ApiV1ProviderAccountsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_2 = (
                        ApiV1ProviderAccountsUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_3 = (
                        ApiV1ProviderAccountsUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_4 = (
                        ApiV1ProviderAccountsUpdateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_5 = (
                        ApiV1ProviderAccountsUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_6 = (
                        ApiV1ProviderAccountsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_7 = (
                        ApiV1ProviderAccountsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_8 = (
                        ApiV1ProviderAccountsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_9 = (
                        ApiV1ProviderAccountsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_10 = (
                        ApiV1ProviderAccountsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_11 = (
                        ApiV1ProviderAccountsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_12 = (
                        ApiV1ProviderAccountsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_13 = (
                        ApiV1ProviderAccountsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_14 = (
                        ApiV1ProviderAccountsUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_15 = (
                        ApiV1ProviderAccountsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_16 = (
                        ApiV1ProviderAccountsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_17 = (
                        ApiV1ProviderAccountsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_18 = (
                        ApiV1ProviderAccountsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_19 = (
                        ApiV1ProviderAccountsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_20 = (
                        ApiV1ProviderAccountsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_21 = (
                        ApiV1ProviderAccountsUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_22 = (
                        ApiV1ProviderAccountsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_23 = (
                        ApiV1ProviderAccountsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_24 = (
                        ApiV1ProviderAccountsUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_25 = (
                        ApiV1ProviderAccountsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_26 = (
                        ApiV1ProviderAccountsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_27 = (
                        ApiV1ProviderAccountsUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_28 = (
                        ApiV1ProviderAccountsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_29 = (
                        ApiV1ProviderAccountsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_30 = (
                        ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_31 = (
                        ApiV1ProviderAccountsUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_32 = (
                        ApiV1ProviderAccountsUpdateApiKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_33 = (
                        ApiV1ProviderAccountsUpdateApiEndpointErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_34 = (
                        ApiV1ProviderAccountsUpdateMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_35 = (
                        ApiV1ProviderAccountsUpdateLastRateLimitedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_36 = (
                        ApiV1ProviderAccountsUpdateApiBackoffMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_37 = (
                        ApiV1ProviderAccountsUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_38 = (
                        ApiV1ProviderAccountsUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_provider_accounts_update_error_type_39 = (
                        ApiV1ProviderAccountsUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_provider_accounts_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_provider_accounts_update_error_type_40 = (
                    ApiV1ProviderAccountsUpdateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_provider_accounts_update_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_provider_accounts_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_provider_accounts_update_validation_error.additional_properties = d
        return api_v1_provider_accounts_update_validation_error

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
