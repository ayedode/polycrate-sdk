from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_datasources_create_annotations_error_component import (
        ApiV1DatasourcesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_datasources_create_archived_at_error_component import (
        ApiV1DatasourcesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_datasources_create_archived_error_component import ApiV1DatasourcesCreateArchivedErrorComponent
    from ..models.api_v1_datasources_create_archived_reason_error_component import (
        ApiV1DatasourcesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_datasources_create_create_incidents_error_component import (
        ApiV1DatasourcesCreateCreateIncidentsErrorComponent,
    )
    from ..models.api_v1_datasources_create_create_incidents_without_resources_error_component import (
        ApiV1DatasourcesCreateCreateIncidentsWithoutResourcesErrorComponent,
    )
    from ..models.api_v1_datasources_create_create_maintenance_as_draft_error_component import (
        ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponent,
    )
    from ..models.api_v1_datasources_create_create_notes_resolved_error_component import (
        ApiV1DatasourcesCreateCreateNotesResolvedErrorComponent,
    )
    from ..models.api_v1_datasources_create_criticality_error_component import (
        ApiV1DatasourcesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_datasources_create_datasource_url_error_component import (
        ApiV1DatasourcesCreateDatasourceUrlErrorComponent,
    )
    from ..models.api_v1_datasources_create_debug_mode_error_component import (
        ApiV1DatasourcesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_datasources_create_display_name_error_component import (
        ApiV1DatasourcesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_datasources_create_is_enabled_error_component import (
        ApiV1DatasourcesCreateIsEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_create_kind_error_component import ApiV1DatasourcesCreateKindErrorComponent
    from ..models.api_v1_datasources_create_labels_error_component import ApiV1DatasourcesCreateLabelsErrorComponent
    from ..models.api_v1_datasources_create_last_sync_error_component import (
        ApiV1DatasourcesCreateLastSyncErrorComponent,
    )
    from ..models.api_v1_datasources_create_last_sync_error_error_component import (
        ApiV1DatasourcesCreateLastSyncErrorErrorComponent,
    )
    from ..models.api_v1_datasources_create_name_error_component import ApiV1DatasourcesCreateNameErrorComponent
    from ..models.api_v1_datasources_create_non_field_errors_error_component import (
        ApiV1DatasourcesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_datasources_create_note_kind_error_component import (
        ApiV1DatasourcesCreateNoteKindErrorComponent,
    )
    from ..models.api_v1_datasources_create_note_organization_id_error_component import (
        ApiV1DatasourcesCreateNoteOrganizationIdErrorComponent,
    )
    from ..models.api_v1_datasources_create_note_workspace_id_error_component import (
        ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponent,
    )
    from ..models.api_v1_datasources_create_platform_service_error_component import (
        ApiV1DatasourcesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_datasources_create_provider_entity_id_error_component import (
        ApiV1DatasourcesCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_datasources_create_provider_error_component import ApiV1DatasourcesCreateProviderErrorComponent
    from ..models.api_v1_datasources_create_provider_id_error_component import (
        ApiV1DatasourcesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_datasources_create_provider_reference_error_component import (
        ApiV1DatasourcesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_datasources_create_reconciliation_enabled_error_component import (
        ApiV1DatasourcesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_create_sla_availability_error_component import (
        ApiV1DatasourcesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_create_sla_target_error_component import (
        ApiV1DatasourcesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_datasources_create_slo_availability_error_component import (
        ApiV1DatasourcesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_create_slo_target_error_component import (
        ApiV1DatasourcesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_datasources_create_sync_interval_minutes_error_component import (
        ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponent,
    )
    from ..models.api_v1_datasources_create_target_availability_error_component import (
        ApiV1DatasourcesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_create_tolerations_error_component import (
        ApiV1DatasourcesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DatasourcesCreateValidationError")


@_attrs_define
class ApiV1DatasourcesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DatasourcesCreateAnnotationsErrorComponent | ApiV1DatasourcesCreateArchivedAtErrorComponent |
            ApiV1DatasourcesCreateArchivedErrorComponent | ApiV1DatasourcesCreateArchivedReasonErrorComponent |
            ApiV1DatasourcesCreateCreateIncidentsErrorComponent |
            ApiV1DatasourcesCreateCreateIncidentsWithoutResourcesErrorComponent |
            ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponent |
            ApiV1DatasourcesCreateCreateNotesResolvedErrorComponent | ApiV1DatasourcesCreateCriticalityErrorComponent |
            ApiV1DatasourcesCreateDatasourceUrlErrorComponent | ApiV1DatasourcesCreateDebugModeErrorComponent |
            ApiV1DatasourcesCreateDisplayNameErrorComponent | ApiV1DatasourcesCreateIsEnabledErrorComponent |
            ApiV1DatasourcesCreateKindErrorComponent | ApiV1DatasourcesCreateLabelsErrorComponent |
            ApiV1DatasourcesCreateLastSyncErrorComponent | ApiV1DatasourcesCreateLastSyncErrorErrorComponent |
            ApiV1DatasourcesCreateNameErrorComponent | ApiV1DatasourcesCreateNonFieldErrorsErrorComponent |
            ApiV1DatasourcesCreateNoteKindErrorComponent | ApiV1DatasourcesCreateNoteOrganizationIdErrorComponent |
            ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponent | ApiV1DatasourcesCreatePlatformServiceErrorComponent |
            ApiV1DatasourcesCreateProviderEntityIdErrorComponent | ApiV1DatasourcesCreateProviderErrorComponent |
            ApiV1DatasourcesCreateProviderIdErrorComponent | ApiV1DatasourcesCreateProviderReferenceErrorComponent |
            ApiV1DatasourcesCreateReconciliationEnabledErrorComponent | ApiV1DatasourcesCreateSlaAvailabilityErrorComponent
            | ApiV1DatasourcesCreateSlaTargetErrorComponent | ApiV1DatasourcesCreateSloAvailabilityErrorComponent |
            ApiV1DatasourcesCreateSloTargetErrorComponent | ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponent |
            ApiV1DatasourcesCreateTargetAvailabilityErrorComponent | ApiV1DatasourcesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DatasourcesCreateAnnotationsErrorComponent
        | ApiV1DatasourcesCreateArchivedAtErrorComponent
        | ApiV1DatasourcesCreateArchivedErrorComponent
        | ApiV1DatasourcesCreateArchivedReasonErrorComponent
        | ApiV1DatasourcesCreateCreateIncidentsErrorComponent
        | ApiV1DatasourcesCreateCreateIncidentsWithoutResourcesErrorComponent
        | ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponent
        | ApiV1DatasourcesCreateCreateNotesResolvedErrorComponent
        | ApiV1DatasourcesCreateCriticalityErrorComponent
        | ApiV1DatasourcesCreateDatasourceUrlErrorComponent
        | ApiV1DatasourcesCreateDebugModeErrorComponent
        | ApiV1DatasourcesCreateDisplayNameErrorComponent
        | ApiV1DatasourcesCreateIsEnabledErrorComponent
        | ApiV1DatasourcesCreateKindErrorComponent
        | ApiV1DatasourcesCreateLabelsErrorComponent
        | ApiV1DatasourcesCreateLastSyncErrorComponent
        | ApiV1DatasourcesCreateLastSyncErrorErrorComponent
        | ApiV1DatasourcesCreateNameErrorComponent
        | ApiV1DatasourcesCreateNonFieldErrorsErrorComponent
        | ApiV1DatasourcesCreateNoteKindErrorComponent
        | ApiV1DatasourcesCreateNoteOrganizationIdErrorComponent
        | ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponent
        | ApiV1DatasourcesCreatePlatformServiceErrorComponent
        | ApiV1DatasourcesCreateProviderEntityIdErrorComponent
        | ApiV1DatasourcesCreateProviderErrorComponent
        | ApiV1DatasourcesCreateProviderIdErrorComponent
        | ApiV1DatasourcesCreateProviderReferenceErrorComponent
        | ApiV1DatasourcesCreateReconciliationEnabledErrorComponent
        | ApiV1DatasourcesCreateSlaAvailabilityErrorComponent
        | ApiV1DatasourcesCreateSlaTargetErrorComponent
        | ApiV1DatasourcesCreateSloAvailabilityErrorComponent
        | ApiV1DatasourcesCreateSloTargetErrorComponent
        | ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponent
        | ApiV1DatasourcesCreateTargetAvailabilityErrorComponent
        | ApiV1DatasourcesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_datasources_create_annotations_error_component import (
            ApiV1DatasourcesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_archived_at_error_component import (
            ApiV1DatasourcesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_archived_error_component import (
            ApiV1DatasourcesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_archived_reason_error_component import (
            ApiV1DatasourcesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_create_incidents_error_component import (
            ApiV1DatasourcesCreateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesCreateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_create_notes_resolved_error_component import (
            ApiV1DatasourcesCreateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_criticality_error_component import (
            ApiV1DatasourcesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_datasource_url_error_component import (
            ApiV1DatasourcesCreateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_debug_mode_error_component import (
            ApiV1DatasourcesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_display_name_error_component import (
            ApiV1DatasourcesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_is_enabled_error_component import (
            ApiV1DatasourcesCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_kind_error_component import (
            ApiV1DatasourcesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_labels_error_component import (
            ApiV1DatasourcesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_last_sync_error_component import (
            ApiV1DatasourcesCreateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_last_sync_error_error_component import (
            ApiV1DatasourcesCreateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_name_error_component import (
            ApiV1DatasourcesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_non_field_errors_error_component import (
            ApiV1DatasourcesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_note_kind_error_component import (
            ApiV1DatasourcesCreateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_note_organization_id_error_component import (
            ApiV1DatasourcesCreateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_note_workspace_id_error_component import (
            ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_platform_service_error_component import (
            ApiV1DatasourcesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_provider_error_component import (
            ApiV1DatasourcesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_provider_id_error_component import (
            ApiV1DatasourcesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_provider_reference_error_component import (
            ApiV1DatasourcesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_reconciliation_enabled_error_component import (
            ApiV1DatasourcesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_sla_availability_error_component import (
            ApiV1DatasourcesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_sla_target_error_component import (
            ApiV1DatasourcesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_slo_availability_error_component import (
            ApiV1DatasourcesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_slo_target_error_component import (
            ApiV1DatasourcesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_sync_interval_minutes_error_component import (
            ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_target_availability_error_component import (
            ApiV1DatasourcesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_tolerations_error_component import (
            ApiV1DatasourcesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DatasourcesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateDatasourceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateNoteKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateNoteOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateCreateNotesResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateCreateIncidentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateCreateIncidentsWithoutResourcesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateLastSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesCreateLastSyncErrorErrorComponent):
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
        from ..models.api_v1_datasources_create_annotations_error_component import (
            ApiV1DatasourcesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_archived_at_error_component import (
            ApiV1DatasourcesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_archived_error_component import (
            ApiV1DatasourcesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_archived_reason_error_component import (
            ApiV1DatasourcesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_create_incidents_error_component import (
            ApiV1DatasourcesCreateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesCreateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_create_notes_resolved_error_component import (
            ApiV1DatasourcesCreateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_criticality_error_component import (
            ApiV1DatasourcesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_datasource_url_error_component import (
            ApiV1DatasourcesCreateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_debug_mode_error_component import (
            ApiV1DatasourcesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_display_name_error_component import (
            ApiV1DatasourcesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_is_enabled_error_component import (
            ApiV1DatasourcesCreateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_kind_error_component import (
            ApiV1DatasourcesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_labels_error_component import (
            ApiV1DatasourcesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_last_sync_error_component import (
            ApiV1DatasourcesCreateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_last_sync_error_error_component import (
            ApiV1DatasourcesCreateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_name_error_component import (
            ApiV1DatasourcesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_non_field_errors_error_component import (
            ApiV1DatasourcesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_note_kind_error_component import (
            ApiV1DatasourcesCreateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_note_organization_id_error_component import (
            ApiV1DatasourcesCreateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_note_workspace_id_error_component import (
            ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_platform_service_error_component import (
            ApiV1DatasourcesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_provider_entity_id_error_component import (
            ApiV1DatasourcesCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_provider_error_component import (
            ApiV1DatasourcesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_provider_id_error_component import (
            ApiV1DatasourcesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_provider_reference_error_component import (
            ApiV1DatasourcesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_reconciliation_enabled_error_component import (
            ApiV1DatasourcesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_sla_availability_error_component import (
            ApiV1DatasourcesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_sla_target_error_component import (
            ApiV1DatasourcesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_slo_availability_error_component import (
            ApiV1DatasourcesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_slo_target_error_component import (
            ApiV1DatasourcesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_sync_interval_minutes_error_component import (
            ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_target_availability_error_component import (
            ApiV1DatasourcesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_create_tolerations_error_component import (
            ApiV1DatasourcesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DatasourcesCreateAnnotationsErrorComponent
                | ApiV1DatasourcesCreateArchivedAtErrorComponent
                | ApiV1DatasourcesCreateArchivedErrorComponent
                | ApiV1DatasourcesCreateArchivedReasonErrorComponent
                | ApiV1DatasourcesCreateCreateIncidentsErrorComponent
                | ApiV1DatasourcesCreateCreateIncidentsWithoutResourcesErrorComponent
                | ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponent
                | ApiV1DatasourcesCreateCreateNotesResolvedErrorComponent
                | ApiV1DatasourcesCreateCriticalityErrorComponent
                | ApiV1DatasourcesCreateDatasourceUrlErrorComponent
                | ApiV1DatasourcesCreateDebugModeErrorComponent
                | ApiV1DatasourcesCreateDisplayNameErrorComponent
                | ApiV1DatasourcesCreateIsEnabledErrorComponent
                | ApiV1DatasourcesCreateKindErrorComponent
                | ApiV1DatasourcesCreateLabelsErrorComponent
                | ApiV1DatasourcesCreateLastSyncErrorComponent
                | ApiV1DatasourcesCreateLastSyncErrorErrorComponent
                | ApiV1DatasourcesCreateNameErrorComponent
                | ApiV1DatasourcesCreateNonFieldErrorsErrorComponent
                | ApiV1DatasourcesCreateNoteKindErrorComponent
                | ApiV1DatasourcesCreateNoteOrganizationIdErrorComponent
                | ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponent
                | ApiV1DatasourcesCreatePlatformServiceErrorComponent
                | ApiV1DatasourcesCreateProviderEntityIdErrorComponent
                | ApiV1DatasourcesCreateProviderErrorComponent
                | ApiV1DatasourcesCreateProviderIdErrorComponent
                | ApiV1DatasourcesCreateProviderReferenceErrorComponent
                | ApiV1DatasourcesCreateReconciliationEnabledErrorComponent
                | ApiV1DatasourcesCreateSlaAvailabilityErrorComponent
                | ApiV1DatasourcesCreateSlaTargetErrorComponent
                | ApiV1DatasourcesCreateSloAvailabilityErrorComponent
                | ApiV1DatasourcesCreateSloTargetErrorComponent
                | ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponent
                | ApiV1DatasourcesCreateTargetAvailabilityErrorComponent
                | ApiV1DatasourcesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_0 = (
                        ApiV1DatasourcesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_1 = (
                        ApiV1DatasourcesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_2 = (
                        ApiV1DatasourcesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_3 = (
                        ApiV1DatasourcesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_4 = (
                        ApiV1DatasourcesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_5 = (
                        ApiV1DatasourcesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_6 = (
                        ApiV1DatasourcesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_7 = (
                        ApiV1DatasourcesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_8 = (
                        ApiV1DatasourcesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_9 = (
                        ApiV1DatasourcesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_10 = (
                        ApiV1DatasourcesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_11 = (
                        ApiV1DatasourcesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_12 = (
                        ApiV1DatasourcesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_13 = (
                        ApiV1DatasourcesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_14 = (
                        ApiV1DatasourcesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_15 = (
                        ApiV1DatasourcesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_16 = (
                        ApiV1DatasourcesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_17 = (
                        ApiV1DatasourcesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_18 = (
                        ApiV1DatasourcesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_19 = (
                        ApiV1DatasourcesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_20 = (
                        ApiV1DatasourcesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_21 = (
                        ApiV1DatasourcesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_22 = (
                        ApiV1DatasourcesCreateDatasourceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_23 = (
                        ApiV1DatasourcesCreateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_24 = (
                        ApiV1DatasourcesCreateSyncIntervalMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_25 = (
                        ApiV1DatasourcesCreateNoteKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_26 = (
                        ApiV1DatasourcesCreateNoteOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_27 = (
                        ApiV1DatasourcesCreateNoteWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_28 = (
                        ApiV1DatasourcesCreateCreateNotesResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_29 = (
                        ApiV1DatasourcesCreateCreateMaintenanceAsDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_30 = (
                        ApiV1DatasourcesCreateCreateIncidentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_31 = (
                        ApiV1DatasourcesCreateCreateIncidentsWithoutResourcesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_32 = (
                        ApiV1DatasourcesCreateLastSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_create_error_type_33 = (
                        ApiV1DatasourcesCreateLastSyncErrorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_datasources_create_error_type_34 = (
                    ApiV1DatasourcesCreateProviderEntityIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_datasources_create_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_datasources_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_datasources_create_validation_error.additional_properties = d
        return api_v1_datasources_create_validation_error

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
