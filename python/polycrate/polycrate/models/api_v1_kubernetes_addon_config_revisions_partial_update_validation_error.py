from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_actual_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_addon_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_annotations_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_archived_at_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_archived_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_archived_reason_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_block_config_template_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateBlockConfigTemplateErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_criticality_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_debug_mode_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_discovery_enabled_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_display_name_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_kind_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_labels_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_name_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_non_field_errors_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_platform_service_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_provider_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_provider_id_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_provider_reference_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_scope_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_sla_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_sla_target_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_slo_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_slo_target_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_target_availability_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_version_error_component import (
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesAddonConfigRevisionsPartialUpdateValidationError")


@_attrs_define
class ApiV1KubernetesAddonConfigRevisionsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesAddonConfigRevisionsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateAnnotationsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedAtErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateBlockConfigTemplateErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateDisplayNameErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateKindErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateLabelsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateNameErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderIdErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateScopeErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaTargetErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloTargetErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesAddonConfigRevisionsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateAnnotationsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedAtErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateBlockConfigTemplateErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateDisplayNameErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateKindErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateLabelsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateNameErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderIdErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateScopeErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaTargetErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloTargetErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_actual_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_addon_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_annotations_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_archived_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_archived_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_archived_reason_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_criticality_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_debug_mode_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_display_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_kind_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_labels_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_platform_service_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_provider_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_provider_id_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_provider_reference_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_scope_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_sla_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_sla_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_slo_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_slo_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_target_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_version_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateDisplayNameErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateAnnotationsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderReferenceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateDiscoveryEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdatePlatformServiceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedReasonErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponent):
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
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_actual_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_addon_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_annotations_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_archived_at_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_archived_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_archived_reason_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_block_config_template_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateBlockConfigTemplateErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_criticality_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_debug_mode_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_display_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_kind_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_labels_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_name_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_platform_service_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_provider_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_provider_id_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_provider_reference_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_scope_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_sla_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_sla_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_slo_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_slo_target_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_target_availability_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_addon_config_revisions_partial_update_version_error_component import (
            ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesAddonConfigRevisionsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateAnnotationsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedAtErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateBlockConfigTemplateErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateDisplayNameErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateKindErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateLabelsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateNameErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderIdErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateScopeErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaTargetErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloTargetErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_0 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_1 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_2 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_3 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_4 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_5 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_6 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_7 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_8 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_9 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateReconciliationEnabledErrorComponent.from_dict(
                            data
                        )
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_10 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_11 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_12 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_13 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_14 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_15 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_16 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_17 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_18 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_19 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_20 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_21 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_22 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_23 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_24 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateAddonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_25 = (
                        ApiV1KubernetesAddonConfigRevisionsPartialUpdateVersionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_26 = (
                    ApiV1KubernetesAddonConfigRevisionsPartialUpdateBlockConfigTemplateErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_addon_config_revisions_partial_update_error_type_26

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_addon_config_revisions_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_addon_config_revisions_partial_update_validation_error.additional_properties = d
        return api_v1_kubernetes_addon_config_revisions_partial_update_validation_error

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
